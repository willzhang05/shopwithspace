import React from 'react';
import { connect } from 'react-redux';

import { hoverResult } from './StoreResultActions';

class StoreResult extends React.Component {
  hoverResult(key) {
    this.props.hoverResult(key);
  }
  render() {
    const hover =
      this.props.marker === this.props.obj.id ? 'result hover' : 'result';
    return (
      <div
        className={hover}
        onMouseEnter={() => this.hoverResult(this.props.obj.id)}
        onMouseLeave={() => this.hoverResult(null)}
      >
        <div className='image'></div>
        <div className='text'>
          <h4>{this.props.obj.name}</h4>

          <span className='coords'>
            {this.props.obj.location.lat}, {this.props.obj.location.lng}
          </span>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    marker: state.marker
  };
};

const mapDispatchToProps = {
  hoverResult
};

export default connect(mapStateToProps, mapDispatchToProps)(StoreResult);
