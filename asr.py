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

    # dump out an SRT
    with open(args.outfile + ".srt", "w") as f:
        for i, s in enumerate(data['segments']):
            print(i + 1, file=f)
            print(timestamp(s['start']), '-->', timestamp(s['end']), file=f)
            print(s['segment'], file=f)
            print(file=f)


def timestamp(t):
    h = int(t / 3600)
    t = t - h * 3600
    m = int(t / 60)
    t = t - m * 60
    s = int(t)
    x = int((t - s)*1000)
    return f"{h:02d}:{m:02d}:{s:02d},{x:03d}"
    

if __name__ == "__main__":
  main()
