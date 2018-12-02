include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?= -v

#> run unit tests
#>   > make test
#>   > make test OPTS="-v -run Day01"
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN' dayNN DayNN

#> go fmt the source
format:
	find src/ -name "*.go" -exec go fmt {} \;

.PHONY: test next format
