#!/bin/bash
chmod +x solution/*.sh
sed -i 's/targetPort: 5000/targetPort: 8080/' service.yaml

