import './App.css';

import SearchBar from './components/SearchBar';
import ReviewList from './components/ReviewList';
import SentimentChart from './components/SentimentChart';
import WordCloud from './components/WordCloud';

function App() {
  return (
    <div className="App">
      <h1>Product Sentiment Analyzer</h1>

      <SearchBar />

      <SentimentChart />

      <ReviewList />

      <WordCloud />
    </div>
  );
}

export default App;