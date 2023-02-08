# XProperties
XProperties is a .properties file parser library, which was written to read/write .properties files in languages other than Java.  
## Install
`pip install XProperties`  
## Documentation
[XProperties Wiki](https://github.com/DuelitDev/XProperties-Python/wiki)  
## Example
```python
# example.py
import XProperties


prop = XProperties.Properties()
prop.load("example.properties")
print(prop["example"])
```  
## Copyright
Copyright 2023. DuelitDev all rights reserved.  
## License
[LGPL-2.1 License](https://github.com/DuelitDev/XProperties/blob/master/LICENSE)  
