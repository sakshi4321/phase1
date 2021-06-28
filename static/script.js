

var filtersConfig = {
  // instruct TableFilter location to import ressources from
  base_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/',
  col_1: 'select',
  
  col_3: 'select',
  col_4:  'checklist',
  col_5:'select',
  alternate_rows: true,
  rows_counter: false,
  btn_reset: true,
  loader: true,
  mark_active_columns: true,
  highlight_keywords: true,
  no_results_message: true,
  col_types: [
    'string', 'string', { type: 'date', locale: 'en-GB', format: ['{yyyy|yy}-{MM}-{dd}'] },
    'string', 'number', 'number',
    'number', 'number', 'number'
  ],
  
  col_widths: [
    '150px', '100px', '100px',
    '70px', '100px', '70px',
    '70px', '60px', '60px'
  ],
  extensions: [{
    name: 'sort',
    images_path: 'https://unpkg.com/tablefilter@latest/dist/tablefilter/style/themes/'
  }]
};

var tf = new TableFilter('table', filtersConfig);
tf.init();
