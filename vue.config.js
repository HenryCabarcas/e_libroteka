const path = require('path')

module.exports = {
    chainWebpack: config => {
        const types = ['vue-modules', 'vue', 'normal-modules', 'normal']
        types.forEach(type => addStyleResource(config.module.rule('css').oneOf(type)))
    },
    devServer: {
        // Fixing issue with WDS disconnected and sockjs network error
        host: '0.0.0.0',
        public: '0.0.0.0:8080',
        disableHostCheck: true,
        // End of fix
    }
}

function addStyleResource(rule) {
    rule.use('style-resource')
        .loader('style-resources-loader')
        .options({
            patterns: [
                path.resolve(__dirname, './src/index.css'),
            ],
        })
}