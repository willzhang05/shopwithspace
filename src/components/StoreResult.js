import React from 'react';
import { connect } from 'react-redux';

import { hoverResult, viewDetailedInfo } from './StoreResultActions';

class StoreResult extends React.Component {
  displayInfo() {
    this.props.viewDetailedInfo(this.props.index);
  }
  hoverResult(key) {
    this.props.hoverResult(key);
  }
  render() {
    const hover =
      this.props.marker === this.props.obj.id ? 'result hover' : 'result';
    let safetyText = '';
    switch (Math.round(this.props.obj.safety)) {
      case 5:
        safetyText = 'safe';
        break;
      case 4:
        safetyText = 'safe';
        break;
      case 3:
        safetyText = 'caution';
        break;
      case 2:
        safetyText = 'unsafe';
        break;
      case 1:
        safetyText = 'unsafe';
        break;
      default:
        break;
    }

    return (
      <div
        className={hover}
        onClick={this.displayInfo.bind(this)}
        onMouseEnter={() => this.hoverResult(this.props.obj.id)}
        onMouseLeave={() => this.hoverResult(null)}
      >
        <div className='image'>
          {/* <img src={this.props.obj.photo} alt='Storefront'></img> */}
        </div>
        <div className='text'>
          <h4>{this.props.obj.name}</h4>

          <span className='address'>
            {this.props.obj.details.formatted_address.substring(
              0,
              this.props.obj.details.formatted_address.indexOf(',')
            )}
          </span>
        </div>
        <div className={'safety r' + Math.round(this.props.obj.safety)}>
          <span className='safety-number'>
            {this.props.obj.safety.toFixed(1)}
          </span>
          <span className='safety-text'>{safetyText}</span>
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
  hoverResult,
  viewDetailedInfo
};

export default connect(mapStateToProps, mapDispatchToProps)(StoreResult);
