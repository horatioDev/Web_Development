# This file is used to script what tests test_prime_function will run
  # py -c "from file_name import function; function(arg1, arg2)"
  # python -c "from file_name import function; function(arg1, arg2)"
    # Run script in terminal: ./test_Prime.sh
     
py -c "from test_prime import test_prime_function; test_prime_function(0, False)"
py -c "from test_prime import test_prime_function; test_prime_function(1, False)"
py -c "from test_prime import test_prime_function; test_prime_function(2, True)"
py -c "from test_prime import test_prime_function; test_prime_function(8, False)"
py -c "from test_prime import test_prime_function; test_prime_function(11, True)"
py -c "from test_prime import test_prime_function; test_prime_function(25, False)"
py -c "from test_prime import test_prime_function; test_prime_function(28, False)"