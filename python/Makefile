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
	docker-compose run --rm test ipython

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.py'
	@../.makefiles/next.sh 'tests/test_dayNN.py' dayNN
	@../.makefiles/next.sh 'tests/input/dayNN.txt'

.PHONY: test shell
