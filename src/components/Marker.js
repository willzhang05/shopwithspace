import React from 'react';
import { connect } from 'react-redux';

import { hoverMarker } from './MarkerActions';

class Marker extends React.Component {
  displayInfo() {
    alert('HI');
  }
  hoverMarker(key) {
    this.props.hoverMarker(key);
  }
  render() {
    let over = 'marker-container';
    let hover = 'marker';

    if (this.props.result === this.props.obj.id) {
      hover = 'market hover';
      over = 'marker-container over';
    } else if (this.props.marker === this.props.obj.id) {
      over = 'marker-container over';
    }
    return (
      <div className={over}>
        <div
          className={hover}
          onClick={this.displayInfo.bind(this)}
          onMouseEnter={() => this.hoverMarker(this.props.obj.id)}
          onMouseLeave={() => this.hoverMarker(null)}
        >
          <div className='marker-icon-container'>
            <div className='marker-icon'>
              <i className='fad fa-store'></i>

              <div className='marker-info'>
                <h4>{this.props.obj.name}</h4>
              </div>
            </div>

            <div className='marker-triangle'></div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    result: state.result,
    marker: state.marker
  };
};

const mapDispatchToProps = {
  hoverMarker
};

export default connect(mapStateToProps, mapDispatchToProps)(Marker);
