include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?= -vv

#> run unit tests
#>   > make test
#>   > make test OPTS="-vvx -k tests/test_day01.py"
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

shell: | build
	docker-compose run --rm test sh -c "cd /app/src; ipython"

edit: | _var_DAY
	vim -O src/day$(DAY).py tests/test_day$(DAY).py

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.py'
	@../.makefiles/next.sh 'tests/test_dayNN.py' dayNN

clean::
	rm -rf prof/

.PHONY: test shell next clean shell open
