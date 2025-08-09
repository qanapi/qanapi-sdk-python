# Changelog

## 1.9.0 (2025-08-09)

Full Changelog: [v1.8.1...v1.9.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.8.1...v1.9.0)

### Features

* **client:** support file upload requests ([5d04380](https://github.com/qanapi/qanapi-sdk-python/commit/5d04380fda8d0a47206d3acbc7ac4b7aebf6fea9))


### Chores

* **internal:** fix ruff target version ([f736edc](https://github.com/qanapi/qanapi-sdk-python/commit/f736edcf5242102b187db2944ce8550b2a69a4c2))
* **internal:** update comment in script ([8017d63](https://github.com/qanapi/qanapi-sdk-python/commit/8017d6349c26383d475538149727e12d4af78793))
* **project:** add settings file for vscode ([e1e08f5](https://github.com/qanapi/qanapi-sdk-python/commit/e1e08f58e5171802adf3fa55e7043cd0c92a0fe5))
* update @stainless-api/prism-cli to v5.15.0 ([99738be](https://github.com/qanapi/qanapi-sdk-python/commit/99738be22bebac558ef0463fae36e0da6d018eda))

## 1.8.1 (2025-07-23)

Full Changelog: [v1.8.0...v1.8.1](https://github.com/qanapi/qanapi-sdk-python/compare/v1.8.0...v1.8.1)

### Bug Fixes

* **parsing:** parse extra field types ([80a6458](https://github.com/qanapi/qanapi-sdk-python/commit/80a645806393c373e90835920d32c694b252cb8c))

## 1.8.0 (2025-07-22)

Full Changelog: [v1.7.4...v1.8.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.7.4...v1.8.0)

### Features

* clean up environment call outs ([08b0373](https://github.com/qanapi/qanapi-sdk-python/commit/08b0373c2e02011e02efe30e9744d2325efd9426))


### Bug Fixes

* **parsing:** ignore empty metadata ([fa708c8](https://github.com/qanapi/qanapi-sdk-python/commit/fa708c8c4dc5992968be85990cc4152bf685029a))

## 1.7.4 (2025-07-12)

Full Changelog: [v1.7.3...v1.7.4](https://github.com/qanapi/qanapi-sdk-python/compare/v1.7.3...v1.7.4)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([af90a8d](https://github.com/qanapi/qanapi-sdk-python/commit/af90a8daa7b3785cd4d3e19d8d2794a2249f5547))


### Chores

* **readme:** fix version rendering on pypi ([fd5f07b](https://github.com/qanapi/qanapi-sdk-python/commit/fd5f07b58eae6633eccbe9b06217d3ad508e4e7d))

## 1.7.3 (2025-07-10)

Full Changelog: [v1.7.2...v1.7.3](https://github.com/qanapi/qanapi-sdk-python/compare/v1.7.2...v1.7.3)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([93abc4f](https://github.com/qanapi/qanapi-sdk-python/commit/93abc4fd5554223264ad62727f75aff90856b410))


### Chores

* **ci:** change upload type ([b68336d](https://github.com/qanapi/qanapi-sdk-python/commit/b68336dc68070062e342a7e224608dc0b77dac6b))
* **internal:** bump pinned h11 dep ([9ea9291](https://github.com/qanapi/qanapi-sdk-python/commit/9ea92914f2ea9b40dfd1e024cec2db4971c4f5be))
* **internal:** codegen related update ([c092f11](https://github.com/qanapi/qanapi-sdk-python/commit/c092f1133ca310bcbc72af6feba436893f3abab9))
* **package:** mark python 3.13 as supported ([675e911](https://github.com/qanapi/qanapi-sdk-python/commit/675e911cd59df3f6eed5b5300ddb0502eed10364))

## 1.7.2 (2025-06-30)

Full Changelog: [v1.7.1...v1.7.2](https://github.com/qanapi/qanapi-sdk-python/compare/v1.7.1...v1.7.2)

### Bug Fixes

* **ci:** correct conditional ([545c36c](https://github.com/qanapi/qanapi-sdk-python/commit/545c36c50372857194a604b6fd5772cce3131a57))


### Chores

* **ci:** only run for pushes and fork pull requests ([dcbb444](https://github.com/qanapi/qanapi-sdk-python/commit/dcbb444243b83e47f73e2e2e4764f8b4cfb28f62))

## 1.7.1 (2025-06-27)

Full Changelog: [v1.7.0...v1.7.1](https://github.com/qanapi/qanapi-sdk-python/compare/v1.7.0...v1.7.1)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([8dc138f](https://github.com/qanapi/qanapi-sdk-python/commit/8dc138f411b91f94037d5806554c42dba8c7d57e))


### Chores

* **tests:** skip some failing tests on the latest python versions ([89b3472](https://github.com/qanapi/qanapi-sdk-python/commit/89b3472ce0b2ffc82f8b644e9a8f04621a4794ea))

## 1.7.0 (2025-06-21)

Full Changelog: [v1.6.1...v1.7.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.6.1...v1.7.0)

### Features

* **client:** add support for aiohttp ([2eed6ca](https://github.com/qanapi/qanapi-sdk-python/commit/2eed6cab33fa770b3f2489ce4e5c872a64d28a8d))

## 1.6.1 (2025-06-19)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/qanapi/qanapi-sdk-python/compare/v1.6.0...v1.6.1)

### Documentation

* **client:** fix httpx.Timeout documentation reference ([bfd5bc1](https://github.com/qanapi/qanapi-sdk-python/commit/bfd5bc102f895ce18c41a226f2e2e08831c1290c))

## 1.6.0 (2025-06-18)

Full Changelog: [v1.5.4...v1.6.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.5.4...v1.6.0)

### Features

* **api:** update via SDK Studio ([c5af39e](https://github.com/qanapi/qanapi-sdk-python/commit/c5af39e9af32368c0fa41471f27c93419f2a36ea))

## 1.5.4 (2025-06-18)

Full Changelog: [v1.5.3...v1.5.4](https://github.com/qanapi/qanapi-sdk-python/compare/v1.5.3...v1.5.4)

## 1.5.3 (2025-06-18)

Full Changelog: [v1.5.2...v1.5.3](https://github.com/qanapi/qanapi-sdk-python/compare/v1.5.2...v1.5.3)

## 1.5.2 (2025-06-18)

Full Changelog: [v1.5.1...v1.5.2](https://github.com/qanapi/qanapi-sdk-python/compare/v1.5.1...v1.5.2)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([66f6b2c](https://github.com/qanapi/qanapi-sdk-python/commit/66f6b2c0377f3c538d12a574c3d52db94730d2bc))


### Chores

* **readme:** update badges ([dfebeef](https://github.com/qanapi/qanapi-sdk-python/commit/dfebeefd9171a908969377e73b33116067c26100))

## 1.5.1 (2025-06-17)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/qanapi/qanapi-sdk-python/compare/v1.5.0...v1.5.1)

## 1.5.0 (2025-06-17)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** update via SDK Studio ([f3ee61c](https://github.com/qanapi/qanapi-sdk-python/commit/f3ee61ce2d37a75397397c01301e07add5295d36))

## 1.4.0 (2025-06-17)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** update via SDK Studio ([f2e5955](https://github.com/qanapi/qanapi-sdk-python/commit/f2e59558c1b6456b51e2fc17d6fb19ca9459e109))

## 1.3.0 (2025-06-17)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** update via SDK Studio ([f29fb3b](https://github.com/qanapi/qanapi-sdk-python/commit/f29fb3b6d8c1bdfd4a6c7a7b735e96e02a886677))

## 1.2.0 (2025-06-17)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** update via SDK Studio ([3e742e7](https://github.com/qanapi/qanapi-sdk-python/commit/3e742e79c759f7595f14a30661ef7b6042379eb9))
* **api:** update via SDK Studio ([1dd3709](https://github.com/qanapi/qanapi-sdk-python/commit/1dd3709beba0fe0f3959b1fc0ed124cb16300d3b))


### Bug Fixes

* **client:** correctly parse binary response | stream ([9601dd9](https://github.com/qanapi/qanapi-sdk-python/commit/9601dd9918b1da722b94ab401440d419ee120d0d))


### Chores

* **ci:** enable for pull requests ([503202e](https://github.com/qanapi/qanapi-sdk-python/commit/503202e9de0fdf75e5dd7a588640f273c35af66e))
* **internal:** update conftest.py ([8aaccce](https://github.com/qanapi/qanapi-sdk-python/commit/8aaccce8f6a15f3d8fe91fd138042abde66e6b9d))
* **tests:** add tests for httpx client instantiation & proxies ([bda3b2d](https://github.com/qanapi/qanapi-sdk-python/commit/bda3b2dd02711a41b08438fc644d61bac5edbd65))
* **tests:** run tests in parallel ([b85982b](https://github.com/qanapi/qanapi-sdk-python/commit/b85982bd5235492e0595df8300c83fd24693523a))

## 1.1.0 (2025-06-11)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/qanapi/qanapi-sdk-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** update via SDK Studio ([60b0f16](https://github.com/qanapi/qanapi-sdk-python/commit/60b0f16eeb2102b4858ed91926ffec0bc79d7f31))
* **api:** update via SDK Studio ([2724e88](https://github.com/qanapi/qanapi-sdk-python/commit/2724e88d0347e5ea8796521d58912aba9729f39c))


### Chores

* **internal:** version bump ([b6f413f](https://github.com/qanapi/qanapi-sdk-python/commit/b6f413f0c92ba2d5a4ffa6181a67687cbdf4b245))

## 1.0.0 (2025-06-10)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/qanapi/qanapi-sdk-python/compare/v0.0.1-alpha.0...v1.0.0)

### Chores

* configure new SDK language ([b24ac37](https://github.com/qanapi/qanapi-sdk-python/commit/b24ac37a35207f8fb73f306606c8fff1022df777))
* update SDK settings ([3ac9dc0](https://github.com/qanapi/qanapi-sdk-python/commit/3ac9dc01c1b1e380d82f6b08f70ebfe472142d14))
* update SDK settings ([3cafbc6](https://github.com/qanapi/qanapi-sdk-python/commit/3cafbc6ac38459ec1ead899ebc5012b999828cb1))
