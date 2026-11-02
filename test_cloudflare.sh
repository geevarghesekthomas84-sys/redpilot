date_check=$(date +%Y-%m-%d)
if [[ $(cat wrangler.toml | grep compatibility_date) == *"$date_check"* ]]; then
  echo "Wrangler date matches current date."
else
  echo "Wrangler date does not match current date."
fi
