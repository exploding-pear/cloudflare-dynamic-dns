if [[ -z "$version" ]]; then
  echo "version variable is empty, must be set"
  exit 1
fi

docker buildx build --platform=linux/arm64,linux/amd64 \
-t rowdymarshmallow/cloudflare-dynamic-dns:${version} .

docker push rowdymarshmallow/cloudflare-dynamic-dns:${version}