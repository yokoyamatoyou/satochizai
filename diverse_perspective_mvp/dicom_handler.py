import os
import io
import datetime
from typing import List

import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid
from dicomweb_client.api import DICOMwebClient


def load_dicom_file(file_obj) -> pydicom.Dataset:
    """Read a DICOM file from a file-like object."""
    return pydicom.dcmread(file_obj)


def retrieve_dicom_web(base_url: str, study_uid: str, out_dir: str) -> List[str]:
    """Retrieve DICOM instances via DICOMweb and save them under out_dir."""
    client = DICOMwebClient(url=base_url)
    instances = client.retrieve_study(study_uid)
    paths = []
    for idx, ds in enumerate(instances):
        path = os.path.join(out_dir, f"{study_uid}_{idx}.dcm")
        ds.save_as(path)
        paths.append(path)
    return paths


def retrieve_dicom_scu(*args, **kwargs):
    """Placeholder for DICOM C-GET/C-MOVE retrieval."""
    raise NotImplementedError("SCU retrieval not implemented in this prototype")


def save_overlay(ds: pydicom.Dataset, overlay_array, output_path: str) -> str:
    """Save overlay data into a DICOM file."""
    ds.OverlayData = overlay_array.tobytes()
    ds.add_new(0x60000010, 'US', overlay_array.shape[1])
    ds.add_new(0x60000011, 'US', overlay_array.shape[0])
    ds.save_as(output_path)
    return output_path


def create_dicom_sr(text: str, output_path: str) -> str:
    """Create a basic text DICOM SR file with the given text."""
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.88.11'
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    ds = FileDataset(output_path, {}, file_meta=file_meta, preamble=b'\0' * 128)
    ds.SOPClassUID = file_meta.MediaStorageSOPClassUID
    ds.SOPInstanceUID = file_meta.MediaStorageSOPInstanceUID
    now = datetime.datetime.now()
    ds.StudyDate = now.strftime('%Y%m%d')
    ds.ContentDate = ds.StudyDate
    ds.Modality = 'SR'
    ds.SeriesInstanceUID = generate_uid()
    ds.StudyInstanceUID = generate_uid()
    item = Dataset()
    item.ValueType = 'Text'
    item.TextValue = text
    ds.ContentSequence = [item]
    ds.save_as(output_path)
    return output_path
