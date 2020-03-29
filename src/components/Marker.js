import React from 'react';
import { connect } from 'react-redux';

import { hoverMarker } from './MarkerActions';

class Marker extends React.Component {
  componentDidMount() {
    // https://icons.duckduckgo.com/ip3/www.walmart.com.ico
    //<img src="https://icons.duckduckgo.com/ip3/{this.props.obj}.ico"/>
  }
  displayInfo() {
    alert('HI');
  }
  hoverMarker() {
    this.props.hoverMarker(this.props.index);
  }
  render() {
    return (
      <div className='marker-container'>
        <div
          className='marker'
          onClick={this.displayInfo.bind(this)}
          onMouseOver={this.hoverMarker.bind(this)}
          onMouseOver={this.hoverMarker.bind(this)}
        >
          <div className='marker-icon-container'>
            <div className='marker-icon'>
              <i className='fad fa-store'></i>

              <div className='marker-info'>
                <h4>{this.props.obj.name}</h4>
                <div>
                  <span>343</span>
                </div>
              </div>
            </div>

            <div className='marker-triangle'></div>
          </div>
          {/* {this.props.obj.name} */}
          {/* <span className='tooltiptext'>This is a test</span> */}
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = {
  hoverMarker
};

export default connect(null, mapDispatchToProps)(Marker);
