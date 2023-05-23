pipeline {
  agent any

  stages {
    stage('Install Plugins') {
      steps {
        script {
          installPlugin('job-dsl')
        }
      }
    }

    stage('Add Job') {
      steps {
        script {
          // Define your job DSL script
          def jobDSLScript = '''
            job('MyJob') {
              steps {
                // Define the steps of your job
                echo 'Hello, Jenkins!'
              }
            }
          '''

          // Create the job using the DSL script
          createJobFromDSL(jobDSLScript)
        }
      }
    }
  }
}

def installPlugin(pluginName) {
  try {
    // Install the plugin if it's not already installed
    if (!Jenkins.instance.pluginManager.getPlugin(pluginName)) {
      Jenkins.instance.updateCenter.getPlugin(pluginName).deploy().get()
      println "Installed plugin: $pluginName"
    } else {
      println "Plugin $pluginName is already installed"
    }
  } catch (Exception e) {
    println "Failed to install plugin: $pluginName"
    throw e
  }
}

def createJobFromDSL(dslScript) {
  try {
    // Import the necessary classes
    import javaposse.jobdsl.plugin.*

    // Create a new instance of the Job DSL plugin
    JobManagement jobManagement = new JenkinsJobManagement()

    // Execute the DSL script to create the job
    JobBuilder.executeDslScript(jobManagement, dslScript)
    println "Job created successfully"
  } catch (Exception e) {
    println "Failed to create job: ${e.message}"
    throw e
  }
}
