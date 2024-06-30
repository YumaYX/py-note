default: clean
	sh make_index.sh > index.markdown

clean:
	-rm -f *.markdown

pub:
	make clean
	make commit

commit:
	git status
	sleep 5
	git add .
	git commit -am 'update'
