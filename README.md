## Build Docker Image
~~~
docker build . --tag=myob-code-test:latest
~~~

## How to run it:
~~~
docker run -it --rm myob-code-test:latest /app/payslip_gen.py --name Steve --amount 60000
~~~


## Run tests:
~~~
docker run -it --rm myob-code-test:latest pytest -v
~~~
