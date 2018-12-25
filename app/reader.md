1.实现注册
    1.1 实现不同用户的教研注册，用户的
{"account": "666@qq.com","password": "123456","type":100,"nickname":"李小刚"}
"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0NTU0NDYxNSwiZXhwIjoxNTQ3MjcyNjE1fQ.eyJpZCI6MSwidHlwZSI6MTAwLCJzY29wZSI6IlVzZXJTY29wZSJ9.1KJXptIlfGLjI_ym2byKwpP0yo0FErvnShDSyMQtb-Cw6k9rG4sEYE_nNrGNe5R6oYrPrEECfIowiUMkisA_HQ"

2.实现登录
    2.1所谓的实现登录，核心就是生成token，让以后的请求接口携带token，验证token，如果token过期了，则重新登录






    在项目的入口文件配置了配置项目之后（app.config.from_object）,如果在别的模块要使用配置项，则直接使用
current_app.config['xx']
