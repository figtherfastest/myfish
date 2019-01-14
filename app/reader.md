1.实现注册
2.实现登录
    2.1所谓的实现登录，核心就是生成token，让以后的请求接口携带token，验证token，如果token过期了，则重新登录
    2.2 前端在加密的时候，应该使用base64的bota加密，由于后端使用的是basic auth的加密方式，但是这种的加密方式是有缺点的，就是安全性比较低，把所有的加密字符串都都放在了前端的header之中，
    




    在项目的入口文件配置了配置项目之后（app.config.from_object）,如果在别的模块要使用配置项，则直接使用
current_app.config['xx']
