
---

### `scripts/upload_to_s3.sh`
```bash
#!/bin/bash
BUCKET=$1
FILE=$2

aws s3 cp ./images/$FILE s3://$BUCKET/
