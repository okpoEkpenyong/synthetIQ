const StarRating = ({ rating, maxStars, title, value }) => {
  const fullStars = Math.floor(rating)
  const halfStar = rating % 1 !== 0

  const stars = Array.from({ length: maxStars }, (_, index) => {
    if (index < fullStars) {
      return <span key={index}>&#9733;</span> // Full star
    } else if (index === fullStars && halfStar) {
      return <span key={index}>&#9734;&#9733;</span> // Half star
    } else {
      return <span key={index}>&#9734;</span> // Empty star
    }
  })

  return (
    <div>
      {title}: {value} {stars}
    </div>
  )
}

export default StarRating
