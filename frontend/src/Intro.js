import React from 'react';
import Container from '@material-ui/core/Container';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

function Intro() {
    return (
        <div>
            <Container maxWidth="md">
                <Paper elevation={3}>
                    <Grid container spacing={2} justify="center" alignItems="center">
                        <Grid item xs={10} style={{ textAlign: "center" }}>
                            <h1>Welcome To My Basic Flask-React App!</h1>
                        </Grid>
                        <Grid item xs={10} style={{ textAlign: "center" }}>
                            <p>
                                It had been a while since I had bootstrapped an application from scratch. Therefore,
                                I spent the last few days trying to do exactly that!
                            </p>

                            <p>
                                I present to you a fully functional basic Flask and React app. You can look at the source code
                                for this application on my Github. Below is the project link:
                            </p>
                            <a href="https://github.com/sananaamir/flask-basic-app" target="_blank">Sanan's Basic Flask-React App</a>
                        </Grid>
                    </Grid>
                </Paper>
            </Container>
        </div>
    );
}

export default Intro;
