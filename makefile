

all: build


# Useful targets to run
build: pyjamas webpy
	pyjamas-0.8alpha1/bin/pyjsbuild -d resgen_web.py -o static -j js/swfobject.js -j js/downloadify.min.js
	cp -rf downloadify/js static
	cp -rf downloadify/media static
	cp -rf downloadify/images static
	@echo "Please open `pwd`/static/resgen_web.html in your preferred browser."
serve: build
	@echo "Please open localhost:8080 in your preferred browser."
	python resgen_serve.py



# Support targets
pyjamas: pyjamas-0.8alpha1
	( cd $< && python ./bootstrap.py)

pyjamas-0.8alpha1:
	tar -xf $@.tar.bz2

webpy: web.py-0.35
	ln -fs $< webpy

web.py-0.35:
	tar -xf $@.tar.gz

downloadify: dcneiner-Downloadify-f96cbe7
	ln -fs $< downloadify

dcneiner-Downloadify-f96cbe7:
	unzip dcneiner-Downloadify-0.2.1-0-g652377f.zip


.PHONY:clean
clean:
	rm -rf static webpy web.py-0.35 pyjamas-0.8alpha1 dcneiner-Downloadify-f96cbe7 downloadify
