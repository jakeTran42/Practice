import React, { Component } from 'react';
import logo from './logo.svg';
import z2 from './z2icon.ico';
import sharingan from './tomoe.png';
import Hello from './TestCom/Hello';
import './App.css';

class App extends Component {

  state = {
    characters: [
      { name: 'Zero Two' || 'Goro', code: '002' },
      { name: 'Hiro', code: '016' },
      { name: 'Ichigo', code: '015' }
    ]
  }

  switchNameHandler = (newCharacter) => {
    {/* DO NOT DO THIS WAY, SHOULD NOT MUTATE STATE THIS WAY this.state.person[0].name = 'Kokoro' */}

    this.setState({
      characters: [
        { name: newCharacter, code: '056' },
        { name: 'Ikuno', code: '196' },
        { name: 'Futoshi', code: '214' }
      ]
    })
  }

  nameChangeHandler = (event) => {
    this.setState({
      characters: [
        { name: 'Goro', code: '056' },
        { name: event.target.value, code: '196' },
        { name: 'Futoshi', code: '214' }
      ]
    })
  }

  render() {

    {/* This is Inline Style */}
    const style = {
      backgroundColor: 'white',
      font: 'inherit',
      border: '2px solid blue',
      padding: '8px',
      cursor: 'pointer'
    }

    return (
      <div className="App">
        <header className="App-header">
          <img src={sharingan} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>

        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <button style={style} onClick={() => this.switchNameHandler('Goro')}>Switch Character</button>

        <Hello name={this.state.characters[0].name} code={this.state.characters[0].code} click={this.switchNameHandler.bind(this, 'Ruko')} />
        <Hello name={this.state.characters[1].name} code={this.state.characters[1].code} changeName={this.nameChangeHandler} />
        <Hello name={this.state.characters[2].name} code={this.state.characters[2].code} />
      </div>
    );
  }
}

export default App;
