include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?= -vv -m "not slow"
export YEAR := 2020

#> run unit tests
#>   > make test
#>   > make test OPTS="-vvx -k tests/test_day01.py"
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

shell: | build
	docker-compose run -e PYTHONPATH='src' -e DAY='$(DAY)' --rm test ipython -i bin/interactive.py

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.py'
	@../.makefiles/next.sh 'tests/test_dayNN.py' dayNN

clean::
	rm -rf prof/
	git clean -Xfd

.PHONY: test shell next clean
