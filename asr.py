#!/bin/env -S apptainer run --nv nemo.sif
import nemo.collections.asr as nemo_asr
import argparse
import difflib
from pathlib import Path
import re
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Input file")
    parser.add_argument("outfile", help="Output file")
    parser.add_argument("--model_version", choices=['2', '3'], default='2', help="Parakeet model version")
    args = parser.parse_args()
  
    # Download and load the pre-trained BERT-based model
    model = nemo_asr.models.ASRModel.from_pretrained(model_name=f"nvidia/parakeet-tdt-0.6b-v{args.model_version}")
    output = model.transcribe([args.infile], timestamps=True)[0]

    data = {'text': output.text,
            'segments': output.timestamp['segment'],
            'words': output.timestamp['word']}
    
    with open(args.outfile, "w") as f:
       yaml.safe_dump(data, f)


if __name__ == "__main__":
  main()
