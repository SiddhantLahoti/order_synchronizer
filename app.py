"""
Streamlit Web Application for Multi-Customer Order Data Synchronization.
Features robust edge-case handling, pre-flight validation, and execution auditing.
"""

from datetime import datetime
import streamlit as st
from config.profiles import CUSTOMER_PROFILES
from core.engine import process_sync
from core.exceptions import (
    CorruptedFileError,
    InsufficientDataError,
    MissingColumnsError,
    SwappedFilesError,
    NoMatchingOrdersError,
    SyncError
)

# Page Setup
st.set_page_config(
    page_title="Order Data Synchronizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Daily Order Data Synchronizer")
st.markdown("Select a customer tab, upload both Excel files, and synchronize order metrics safely.")

st.divider()

# Dynamically construct customer tabs
profile_keys = list(CUSTOMER_PROFILES.keys())
tab_labels = [
    f"{CUSTOMER_PROFILES[k]['icon']} {CUSTOMER_PROFILES[k]['display_name']}"
    for k in profile_keys
]
tabs = st.tabs(tab_labels)

for idx, profile_key in enumerate(profile_keys):
    profile = CUSTOMER_PROFILES[profile_key]
    
    with tabs[idx]:
        st.subheader(f"{profile['display_name']} Order Processing")
        st.caption(profile["description"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**1. Base Maintained File**")
            file_data = st.file_uploader(
                f"Upload {profile['display_name']} DATA File (.xlsx)",
                type=["xlsx"],
                key=f"data_{profile_key}"
            )
        with col2:
            st.markdown("**2. System Export File**")
            file_workdata = st.file_uploader(
                f"Upload {profile['display_name']} WorkDataNew File (.xlsx)",
                type=["xlsx"],
                key=f"workdata_{profile_key}"
            )

        st.markdown("---")

        if file_data and file_workdata:
            if st.button(
                f"🚀 Run {profile['display_name']} Synchronization",
                type="primary",
                key=f"btn_{profile_key}",
                use_container_width=True
            ):
                with st.spinner(f"Validating and updating {profile['display_name']} data..."):
                    try:
                        output_buf, audit = process_sync(
                            data_file_bytes=file_data,
                            workdata_file_bytes=file_workdata,
                            profile=profile
                        )

                        # Success Header & Metrics
                        st.success(f"✨ {profile['display_name']} synchronization completed successfully!")

                        m1, m2, m3 = st.columns(3)
                        m1.metric("Orders Matched & Updated", audit["updated_count"])
                        m2.metric("Unmatched / Flagged Orders", len(audit["missing_orders"]))
                        m3.metric("Duplicate Source Records", len(audit["duplicate_orders"]))

                        # Download Action
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        download_name = f"{profile['display_name']}_DATA_Updated_{timestamp}.xlsx"

                        st.download_button(
                            label=f"📥 Download Updated {profile['display_name']} File",
                            data=output_buf,
                            file_name=download_name,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )

                        # Advisory Warnings
                        for warn in audit["warnings"]:
                            st.warning(f"⚠️ {warn}")

                        # Missing Orders Table
                        if audit["missing_orders"]:
                            with st.expander(f"📋 View Unmatched Orders ({len(audit['missing_orders'])})", expanded=True):
                                st.dataframe(audit["missing_orders"], use_container_width=True)

                        # Duplicate Orders Table
                        if audit["duplicate_orders"]:
                            with st.expander(f"ℹ️ View Duplicate Source Orders ({len(audit['duplicate_orders'])})"):
                                st.write(audit["duplicate_orders"])

                    # Specific, actionable edge-case error banners
                    except SwappedFilesError as e:
                        st.error(f"🔄 **File Alignment Error:** {str(e)}")
                    except MissingColumnsError as e:
                        st.error(f"📐 **Column Coordinate Error:** {str(e)}")
                    except InsufficientDataError as e:
                        st.error(f"📄 **Incomplete File Error:** {str(e)}")
                    except NoMatchingOrdersError as e:
                        st.error(f"❌ **Lookup Mismatch:** {str(e)}")
                    except CorruptedFileError as e:
                        st.error(f"🔒 **Corrupted/Invalid File:** {str(e)}")
                    except SyncError as e:
                        st.error(f"⚠️ **Processing Error:** {str(e)}")
                    except Exception as e:
                        st.error(f"❗ **Unexpected Error:** An unexpected error occurred: {str(e)}")
        else:
            st.info(f"💡 Please upload both Excel files for {profile['display_name']} to run the synchronizer.")