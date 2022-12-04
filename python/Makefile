include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?= -vv

#> run unit tests
#>   > make test
#>   > make test OPTS="-vvx -k tests/test_day01.py"
test: | build lint
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test


#> run the linter on src and tests
lint: | build
	docker-compose run --rm test black --check src/ tests/


#> format files in src and tests
format: | build
	docker-compose run --rm test black src/ tests/


#> launch an ipython shell in the test environment
shell: | build
	docker-compose run --rm test ipython


#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.py'
	@../.makefiles/next.sh 'tests/test_dayNN.py' dayNN


clean::
	rm -rf prof/


.PHONY: test shell next clean lint format
