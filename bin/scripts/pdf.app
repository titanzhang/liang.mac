#!/bin/sh

#Edit this line to define a path to XLD.app
AAR_APP="/Applications/Adobe Acrobat Reader DC.app"

if [ ! -d "${AAR_APP}" ] ; then
	echo "Acrobat Reader.app not found"
	exit;
fi

"${AAR_APP}/Contents/MacOS/AdobeReader" --cmdline "$@"
