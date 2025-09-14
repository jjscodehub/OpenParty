# OpenParty

OpenParty is a custom Just Dance Unlimited server project made by the Just Dance Party team.

## Features

* **Independence**: The system provides Just Dance Unlimited functionality without reliance on official servers (mostly).

* **Community-Driven Development**: The project's evolution was developed with contributions from the community.

* **Multi-platform Compatibility**: OpenParty supports PC, Nintendo Switch, PlayStation 4/5 (untested) and Wii U (untested).

## Installation

### Prerequisites

* Node.js

* Git

* Server Hosting Environment

### Setup Procedure

1. **Repository Cloning**:

   ```
   git clone [https://github.com/ibratabian17/openparty.git](https://github.com/ibratabian17/openparty.git)
   cd openparty
   ```

2. **Dependency Installation**:

   ```
   npm install
   ```

3. **Server Initialization**:

   ```
   pm2 start server.js --name openparty-server --no-daemon
   ```

## Directory Structure

The OpenParty directory structure is organized to optimize access and facilitate modifications to server functionalities and data. A detailed overview is provided below:

* ### `database/Platforms/openparty-all/songdbs.json`

  * **Purpose**: This file contains the song database.

* ### `database/nohud/chunk.json`

  * **Purpose**: This file contains configurations for every map's video content.

* ### `database/Platforms/{Platform}/sku-packages.json`

  * **Purpose**: This file contains every maps' files.

* ### `core/scripts/run.js`

  * **Purpose**: This script manages the logging operations and automatic restarts.
