

all: build


# Useful targets to run
build: pyjamas webpy
	pyjamas-0.8alpha1/bin/pyjsbuild -d resgen_web.py -o static
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




.PHONY:clean
clean:
	rm -rf static webpy web.py-0.35 pyjamas-0.8alpha1 
