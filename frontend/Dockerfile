# Frontend Dockerfile
FROM node:23-slim

# Set work directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project
COPY . .

# Expose port
EXPOSE 5173

# Command to run the application in dev mode with host mapping
CMD ["npm", "run", "dev", "--", "--host"]
