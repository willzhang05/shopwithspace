import React from 'react';

class Loader extends React.Component {
  render() {
    return (
      <div className='lds-wrapper'>
        <div className='lds-grid'>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
    );
  }
}
export default Loader;
