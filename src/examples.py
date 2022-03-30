# Simple login that uses authorization token
import onehoneonline
onehoneclient = onehoneonline.onehoneclient(token="")
print(f"-- Account user_id is::: {onehoneclient.user_id}")
