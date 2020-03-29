export function hoverMarker(key) {
  return {
    type: 'HOVER_MARKER',
    payload: { key }
  };
}

export function viewDetailedInfo(key) {
  return {
    type: 'VIEW_DETAILED_INFO',
    payload: { key }
  };
}
