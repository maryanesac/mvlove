"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.jdkDownloaderConstants = void 0;
var jdkDownloaderConstants;
(function (jdkDownloaderConstants) {
    jdkDownloaderConstants.ORACLE_JDK_RELEASES_BASE_URL = `https://java.oraclecloud.com/currentJavaReleases`;
    jdkDownloaderConstants.ORACLE_JDK_BASE_DOWNLOAD_URL = `https://download.oracle.com/java`;
    jdkDownloaderConstants.ORACLE_JDK_FALLBACK_VERSIONS = [
        { version: '26', isLts: false },
        { version: '25', isLts: true },
        { version: '21', isLts: true }
    ];
    jdkDownloaderConstants.OPEN_JDK_VERSION_DOWNLOAD_LINKS = {
        "26": "https://download.java.net/java/GA/jdk26.0.2.1/3b8e6c7ec6274148a7aa15e7e7dfb53c/1/GPL/openjdk-26.0.2.1"
    };
})(jdkDownloaderConstants || (exports.jdkDownloaderConstants = jdkDownloaderConstants = {}));
//# sourceMappingURL=constants.js.map