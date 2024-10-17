new Vue({
    el: '#app',
    data: {
        configPath: '',
        astDefaults: {
            debug: false,
            log_level: 'INFO',
            log_file: '/var/log/ast.log',
            output_directory: '/var/lib/ast',
            workers: 4,
            discovery_interval_seconds: 3600,
            data_types: {
                f5_dns: {
                    enabled: false
                },
                f5_gtm: {
                    enabled: false
                }
            },
            tls: {
                insecure_skip_verify: false,
                ca_file: ""
            },
            f5_data_export: false
        },
        bigipReceivers: [],
        envVariables: [],
        envSecrets: []
    },
    methods: {
        saveAstDefaults() {
            fetch('/save_ast_defaults/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({
                    configPath: this.configPath,
                    data: this.astDefaults
                })
            }).then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.error('Error:', error));
        },
        addReceiver() {
            this.bigipReceivers.push({
                name: '',
                endpoint: '',
                username: '',
                password: '',
                collection_interval: '30s',
                data_types: {
                    f5_dns: {
                        enabled: false
                    },
                    f5_gtm: {
                        enabled: false
                    }
                },
                tls: {
                    insecure_skip_verify: false,
                    ca_file: ''
                }
            });
        },
        removeReceiver(index) {
            this.bigipReceivers.splice(index, 1);
        },
        saveBigipReceivers() {
            fetch('/save_bigip_receivers/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({
                    configPath: this.configPath,
                    data: this.bigipReceivers
                })
            }).then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.error('Error:', error));
        },
        addEnvVariable() {
            this.envVariables.push({ key: '', value: '' });
        },
        removeEnvVariable(index) {
            this.envVariables.splice(index, 1);
        },
        saveEnvVariables() {
            fetch('/save_env_variables/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({
                    configPath: this.configPath,
                    data: this.envVariables
                })
            }).then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.error('Error:', error));
        },
        addEnvSecret() {
            this.envSecrets.push({ key: '', value: '' });
        },
        removeEnvSecret(index) {
            this.envSecrets.splice(index, 1);
        },
        saveEnvSecrets() {
            fetch('/save_env_secrets/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({
                    configPath: this.configPath,
                    data: this.envSecrets
                })
            }).then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.error('Error:', error));
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
});