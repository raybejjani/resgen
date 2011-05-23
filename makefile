

all: build

build: pyjamas
	pyjamas-0.8alpha1/bin/pyjsbuild -d resgen_web.py

pyjamas: pyjamas-0.8alpha1
	( cd $< && python ./bootstrap.py)

pyjamas-0.8alpha1:
	tar -xf $@.tar.bz2

.PHONY:clean
clean:
	rm -rf output
