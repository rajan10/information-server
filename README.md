# information-server
The project contains REST api ends 'public ' and 'private' where access to the 'private' web service requires secret key. But for the public resource secret key is not needed and anyone can access it without requiring secret key. 
This project will use JWT from auth server application [Auth](https://github.com/rajan10/auth) that generates JWT token for private resource access. Also Dockerfile is added to create a docker image for this application.

## Table of Contents

-[Installation](#Installation)
-[Usage](#Usage)
-[Contributing](#Contributing)
-[Related project](#Related project)
-[License](#License) 
-[Questions](#Questions)

## Installation
In the virtual env prompt, type
    pip install -r requirements.txt to copy all the required dependencies
## Usage
This is used to test the auth server application that needs JWT token for private resource access.

## Contributing
Anyone can contribute to this project.

## Related project
 -[Auth](https://github.com/rajan10/auth)

## License
This project is not licensed under the [MIT License.](https://mit-license.org/) 
