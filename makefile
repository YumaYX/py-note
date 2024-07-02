default: clean
	sh make_index.sh > index.markdown

test:
	sh make_index.sh
	make clean

clean:
	rm -f *.markdown

pub:
	make test
	make commit

commit:
	git status
	sleep 5
	git add .
	git commit -am 'update'
