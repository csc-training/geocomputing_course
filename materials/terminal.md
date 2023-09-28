# Terminal

## Login with SSH

- SSH is a terminal program that gives you command-line access on the CSC supercomputer
- It is a versatile main interface to a supercomputer
   - Laptop &harr; Toyota, Supercomputer &harr; F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to log in with SSH](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux have SSH. On Windows, Powershell can be used, but we recommend the Puhti web interface, or clients like MobaXterm or PuTTY
   - Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain SSH will not allow displaying remote graphics
   - Puhti web interface is often best for this, but can be enabled also by X11-tunneling (additional installations required on Windows, see link above)

# Advanced topic: Setting up SSH keys

- Using SSH keys is easier and safer than using a password with every login
- SSH keys can be easily used in Windows, Mac, Linux
- Consult our [tutorials on how to set up SSH keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
   - [Logging in to LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) requires setting up an SSH key pair and registering the public key in [My CSC](https:/my.csc.fi)

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via SSH
   - For example, an IDE like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)
- Note that [Visual Studio Code](https://docs.csc.fi/computing/webinterface/vscode/) and [Jupyter Notebooks](https://docs.csc.fi/computing/webinterface/jupyter/) are also available through the Puhti web interface

## File editing