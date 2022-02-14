restartdjango:
	docker-compose restart django

shell:
	docker-compose run django python manage.py shell

restartcaddy:
	docker-compose run caddy caddy reload --config /etc/caddy/Caddyfile 
