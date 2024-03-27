
deploy:
	echo "" >> .env
	echo "APP_ROOT_PATH=/prod" >> .env
	sls deploy --aws-profile <aws-profile>


include .env
export
migrations:
	read -p "Enter migration message: " message; \
	alembic revision --autogenerate -m "$$message"

migrate:
	alembic upgrade head

