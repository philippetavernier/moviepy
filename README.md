# moviepy

quick receipe to install on linux ubuntu 18

## Install
``` sudo apt-get install python3-pip 
 sudo pip3 install setuptools
 sudo pip3 install moviepy
 sudo pip3 install scikit-build
 sudo pip3 install cmake

 sudo pip3 install cython
 sudo pip3 install moviepy[optional]
 sudo apt-get install ffmpeg
```
edit policy.xml

sudo nano /etc/ImageMagick-6/policy.xml

<policymap>
  <!-- <policy domain="resource" name="temporary-path" value="/tmp"/> -->
  <!-- <policy domain="resource" name="memory" value="2GiB"/> -->
  <!-- <policy domain="resource" name="map" value="4GiB"/> -->
  <!-- <policy domain="resource" name="area" value="1GB"/> -->
  <!-- <policy domain="resource" name="disk" value="16EB"/> -->
  <!-- <policy domain="resource" name="file" value="768"/> -->
  <!-- <policy domain="resource" name="thread" value="4"/> -->
  <!-- <policy domain="resource" name="throttle" value="0"/> -->
  <!-- <policy domain="resource" name="time" value="3600"/> -->
  <!-- <policy domain="system" name="precision" value="6"/> -->
  <policy domain="cache" name="shared-secret" value="passphrase"/>
  <policy domain="coder" rights="none" pattern="EPHEMERAL" />
  <policy domain="coder" rights="none" pattern="URL" />
  <policy domain="coder" rights="none" pattern="HTTPS" />
  <policy domain="coder" rights="none" pattern="MVG" />
  <policy domain="coder" rights="none" pattern="MSL" />
  <policy domain="coder" rights="none" pattern="TEXT" />
<policy domain="coder" rights="none" pattern="SHOW" />
  <policy domain="coder" rights="none" pattern="WIN" />
  <policy domain="coder" rights="none" pattern="PLT" />
  <policy domain="path" rights="none" pattern="@*" />
</policymap>

comment out (or remove the line that reads)
<policy domain="path" rights="none" pattern="@*" />

<!-- <policy domain="path" rights="none" pattern="@*" /> -->
