# Nemo python apptainer

This will create an apptainer image with the nemo:25.11 image that 
automatically calls python so it can be used as an interpreter, including
interactively.

The image can be copied to any system which has the apptainer runtime installed.

Some examples can be found at
https://github.com/NVIDIA-NeMo/NeMo/blob/v1.0.0b1/examples/nlp/


## Example Usage

# Capitalize and punctuate 
Given a file `test.py`:
```
#!/bin/env -S apptainer run --nv nemo.sif
from nemo.collections.nlp.models import PunctuationCapitalizationModel

model = PunctuationCapitalizationModel.from_pretrained("punctuation_en_bert")
output = model.add_punctuation_capitalization(["hello world"])
print(output[0])
```    

It can be run as:
`apptainer run --nv nemo.sif test.py`
or, if you're in the container's directory:
`./nemo.sif test.py`




## Notes about disk usage
The nvidia dev image is huge.  The build script should be modified to point to
locations that have an appropriate amount of free space needed during the 
build:

* APPTAINER_CACHEDIR should have at least 30G free
* TMPDIR should have at least 80G free

The resulting image is ~27G
