

all: build

build: pyjamas
	pyjamas-0.8alpha1/bin/pyjsbuild -d resgen_web.py
	@echo "Please open `pwd`/output/resgen_web.html in your favourite browser."

pyjamas: pyjamas-0.8alpha1
	( cd $< && python ./bootstrap.py)

pyjamas-0.8alpha1:
	tar -xf $@.tar.bz2

.PHONY:clean
clean:
	rm -rf output
