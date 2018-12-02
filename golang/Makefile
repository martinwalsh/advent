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
	@../.makefiles/next.sh 'src/dayNN.go' dayNN
	@../.makefiles/next.sh 'src/dayNN_test.go' dayNN DayNN
	@../.makefiles/next.sh 'src/input/dayNN.txt'

#> go fmt the source
format:
	go fmt src/*.go

.PHONY: test next format
