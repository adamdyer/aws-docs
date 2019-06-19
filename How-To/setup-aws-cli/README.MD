# Install Python, pip, and AWS Command Line Interface on Ubuntu

### Ubuntu 18

```sudo apt install awscli```

#### Ubuntu 16

### Install Pip
```
sudo apt install python3-pip
```

### Verify that pip is installed correctly.
```sh
pip3 --version
```

## Install AWS CLI
```
pip3 install awscli --upgrade --user
```

### Check version of AWS CLI
```
aws --version
```

#### To configure aws cli run `aws configure`
You will be prompted to enter four items. Paste in the two keys, and enter your preferred region, say `ap-south-1` and json for the final prompts as shown.
```sh
AWS Access Key ID [None]: AKIAIAY7KGL75O3NTVSA 
AWS Secret Access Key [None]: 2pM59CQnGpUfxm6PD0JFRz/lzwFUHbNBXG4I5yZb
Default region name [None]: ap-south-1
Default output format [None]: json
```
